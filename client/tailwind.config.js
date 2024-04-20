/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    screens: {
      'xl': {'max': '1280px'},
      // => @media (max-width: 1280px) { ... }

      'lg': {'max': '1024px'},
      // => @media (max-width: 1024px) { ... }

      'md': {'max': '900px'},
      // => @media (max-width: 900px) { ... }

      'base': {'max': '639px'},
      // => @media (max-width: 639px) { ... }

      'sm': {'max': '412px'},
      // => @media (max-width: 412px) { ... }
    },
  },
  plugins: [],
}
