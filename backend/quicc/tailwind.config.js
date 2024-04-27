/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './login/templates/login/**/*.html',
    './employee/templates/employee/**/*.html',
    './manager/templates/manager/**/*.html',
    './templates/**/*.html',
    // Add paths to other apps if necessary
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
