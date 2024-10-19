module.exports = {
  ...require('@aittorai/prettier-config-react'),
  overrides: [
    {
      files: ['public/locales/*.json'],
      options: {
        tabWidth: 4,
      },
    },
  ],
};
