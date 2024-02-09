const path = require('path')

module.exports = {
  mode: 'development',
  entry: path.resolve(__dirname, './src/index.jsx'),
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dis'),
  },
  module: {
    rules: [
      {
      test: /\.(js|jsx)$/,
      exclude: /(node_modules|bower_components)/,
      loader: 'babel-loader',
      //what does this do?
      // options: {presets: ["@babel/env"]}
      },
      {
      test: /\.css$/,
      use: ["style-loader", "css-loader"]
      }
    ],
  }
}