# Local Development

If you want to contribute, you will need to set up a [local development environment](./dev-environment.md).

## Documentation

We use [mkdocs](https://www.mkdocs.org) for our documentation with the [material theme](https://squidfunk.github.io/mkdocs-material/). Documentation is written in markdown files under the `./docs` folder and then built into a static website for hosting with GitHub Pages at 

To contribute to the documentation you'll need to install the dependencies. Note
the use of `"`.

```zsh
pip install ".[docs]"
```

Now, to run the documentation locally with hot-reloading for changes made.

```zsh
mkdocs serve
```

You'll then be prompted to connect to `http://127.0.0.1:8080` in order to
access.

## Backend

The backend is contained within the `./aittor/backend` and `./aittor/app` directories.
To get started please install the development dependencies.

From the root of the repository run the following command. Note the use of `"`.

```zsh
pip install ".[dev,test]"
```

These are optional groups of packages which are defined within the `pyproject.toml`
and will be required for testing the changes you make to the code.

### Tests

See the [tests documentation](./TESTS.md) for information about running and writing tests.

### Reloading Changes

Experimenting with changes to the Python source code is a drag if you have to re-start the server —
and re-load those multi-gigabyte models —
after every change.

For a faster development workflow, add the `--dev_reload` flag when starting the server.
The server will watch for changes to all the Python files in the `aittor` directory and apply those changes to the
running server on the fly.

This will allow you to avoid restarting the server (and reloading models) in most cases, but there are some caveats; see
the [jurigged documentation](https://github.com/breuleux/jurigged#caveats) for details.

## Front End

<!--#TODO: get input from blessedcoolant here, for the moment inserted the frontend README via snippets extension.-->

--8<-- "aittor/frontend/web/README.md"

## Developing app in VSCode

VSCode offers some nice tools:

- python debugger
- automatic `venv` activation
- remote dev (e.g. run app on a beefy linux desktop while you type in
  comfort on your macbook)

### Setup

You'll need the
[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
and
[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
extensions installed first.

It's also really handy to install the `Jupyter` extensions:

- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Jupyter Cell Tags](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-cell-tags)
- [Jupyter Notebook Renderers](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers)
- [Jupyter Slide Show](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-slideshow)

#### app workspace

Creating a VSCode workspace for working on app is highly recommended. It
can hold app-specific settings and configs.

To make a workspace:

- Open the App repo dir in VSCode
- `File` > `Save Workspace As` > save it _outside_ the repo

#### Default python interpreter (i.e. automatic virtual environment activation)

- Use command palette to run command
  `Preferences: Open Workspace Settings (JSON)`
- Add `python.defaultInterpreterPath` to `settings`, pointing to your `venv`'s
  python

Should look something like this:

```jsonc
{
  // I like to have all app-related folders in my workspace
  "folders": [
    {
      // repo root
      "path": "Aittor"
    },
    {
      // app root dir, where `aittor.yaml` lives
      "path": "/path/to/app_root"
    }
  ],
  "settings": {
    // Where your app `venv`'s python executable lives
    "python.defaultInterpreterPath": "/path/to/app_root/.venv/bin/python"
  }
}
```

Now when you open the VSCode integrated terminal, or do anything that needs to
run python, it will automatically be in your app virtual environment.

Bonus: When you create a Jupyter notebook, when you run it, you'll be prompted
for the python interpreter to run in. This will default to your `venv` python,
and so you'll have access to the same python environment as the app.

This is _super_ handy.

#### Enabling Type-Checking with Pylance

We use python's typing system in AI. PR reviews will include checking that types are present and correct. We don't enforce types with `mypy` at this time, but that is on the horizon.

Using a code analysis tool to automatically type check your code (and types) is very important when writing with types. These tools provide immediate feedback in your editor when types are incorrect, and following their suggestions lead to fewer runtime bugs.

Pylance, installed at the beginning of this guide, is the de-facto python LSP (language server protocol). It provides type checking in the editor (among many other features). Once installed, you do need to enable type checking manually:

- Open a python file
- Look along the status bar in VSCode for `{ } Python`
- Click the `{ }`
- Turn type checking on - basic is fine

You'll now see red squiggly lines where type issues are detected. Hover your cursor over the indicated symbols to see what's wrong.

In 99% of cases when the type checker says there is a problem, there really is a problem, and you should take some time to understand and resolve what it is pointing out.

#### Debugging configs with `launch.json`

Debugging configs are managed in a `launch.json` file. Like most VSCode configs,
these can be scoped to a workspace or folder.

Follow the [official guide](https://code.visualstudio.com/docs/python/debugging)
to set up your `launch.json` and try it out.

Now we can create the app debugging configs:

```jsonc
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      // Run the app backend & serve the pre-built UI
      "name": "App Web",
      "type": "python",
      "request": "launch",
      "program": "scripts/app-web.py",
      "args": [
        // Your app root dir (where `aittor.yaml` lives)
        "--root",
        "/path/to/app_root",
        // Access the app from anywhere on your local network
        "--host",
        "0.0.0.0"
      ],
      "justMyCode": true
    },
    {
      // Run the nodes-based CLI
      "name": "App CLI",
      "type": "python",
      "request": "launch",
      "program": "scripts/app-cli.py",
      "justMyCode": true
    },
    {
      // Run tests
      "name": "App Test",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["--capture=no"],
      "justMyCode": true
    },
    {
      // Run a single test
      "name": "App Single Test",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": [
        // Change this to point to the specific test you are working on
        "tests/nodes/test_operator.py"
      ],
      "justMyCode": true
    },
    {
      // This is the default, useful to just run a single file
      "name": "Python: File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "justMyCode": true
    }
  ]
}
```

You'll see these configs in the debugging configs drop down. Running them will
start app with attached debugger, in the correct environment, and work just
like the normal app.

Enjoy debugging app with ease (not that we have any bugs of course).

#### Remote dev

This is very easy to set up and provides the same very smooth experience as
local development. Environments and debugging, as set up above, just work,
though you'd need to recreate the workspace and debugging configs on the remote.

Consult the
[official guide](https://code.visualstudio.com/docs/remote/remote-overview) to
get it set up.

Suggest using VSCode's included settings sync so that your remote dev host has
all the same app settings and extensions automatically.

##### One remote dev gotcha

I've found the automatic port forwarding to be very flakey. You can disable it
in `Preferences: Open Remote Settings (ssh: hostname)`. Search for
`remote.autoForwardPorts` and untick the box.

To forward ports very reliably, use SSH on the remote dev client (e.g. your
macbook). Here's how to forward both backend API port (`9090`) and the frontend
live dev server port (`5173`):

```bash
ssh \
    -L 9090:localhost:9090 \
    -L 5173:localhost:5173 \
    user@remote-dev-host
```

The forwarding stops when you close the terminal window, so suggest to do this
_outside_ the VSCode integrated terminal in case you need to restart VSCode for
an extension update or something

Now, on your remote dev client, you can open `localhost:9090` and access the UI,
now served from the remote dev host, just the same as if it was running on the
client.
