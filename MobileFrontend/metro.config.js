const { getDefaultConfig } = require('@expo/metro-config');
const defaultConfig = getDefaultConfig(__dirname);
defaultConfig.resolver.assetExts.push('ort');
defaultConfig.resolver.assetExts.push('config');
defaultConfig.resolver.assetExts.push('json');
defaultConfig.resolver.assetExts.push('txt');
defaultConfig.resolver.unstable_enablePackageExports = true;
defaultConfig.resolver.unstable_conditionNames = ['require']
module.exports = defaultConfig;