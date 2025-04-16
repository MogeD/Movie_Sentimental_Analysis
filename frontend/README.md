# Movie Sentiment Analyzer Frontend

A React-based frontend for the Movie Sentiment Analysis project.

## Features

- Clean, modern UI built with Material-UI
- Real-time sentiment analysis of movie reviews
- Analysis history tracking
- Responsive design for all screen sizes

## Technologies Used

- React 18
- TypeScript
- Material-UI
- Axios for API communication

## Setup

1. Install dependencies:

```bash
npm install
```

2. Start the development server:

```bash
npm start
```

The application will be available at `http://localhost:3000`

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── App.tsx
│   └── index.tsx
├── package.json
├── tsconfig.json
└── README.md
```

## Development

The frontend communicates with the FastAPI backend running on `http://localhost:8000`. Make sure the backend server is running before using the application.

## Building for Production

To create a production build:

```bash
npm run build
```

This will create an optimized build in the `build` directory.
