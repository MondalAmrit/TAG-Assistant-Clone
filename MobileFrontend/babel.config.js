module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
    plugins: ['@babel/plugin-syntax-import-meta',
              '@babel/plugin-proposal-numeric-separator' // Remove for hermes engine
    ],
  };
};
