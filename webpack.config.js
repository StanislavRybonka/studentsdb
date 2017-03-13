var path = require('path');

module.exports = {
  entry: ['./static/js/main.js','./static/js/react.js'],
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, './static/dist')
  },
     module: {
    rules: [
      {test: /\.(js|jsx)$/, use: 'babel-loader'}
    ]
  },
};
