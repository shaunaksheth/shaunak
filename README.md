# Angular Login Application

This project has been converted from a plain HTML form to a full Angular application that communicates with the Python login service.

## Project Structure

```
├── src/
│   ├── app/
│   │   ├── components/
│   │   │   └── login/
│   │   │       ├── login.component.ts
│   │   │       ├── login.component.html
│   │   │       └── login.component.css
│   │   ├── services/
│   │   │   └── auth.service.ts
│   │   ├── app.component.ts
│   │   └── app.component.css
│   ├── main.ts
│   ├── index.html
│   └── styles.css
├── angular.json
├── tsconfig.json
├── tsconfig.app.json
├── package.json
├── login_service.py      (Python backend service)
├── login.html            (Old HTML version)
└── README.md             (This file)
```

## Setup Instructions

### Prerequisites
- Node.js (v18 or higher) and npm
- Python 3.6+
- Angular CLI (will be installed with npm)

### 1. Install Angular Dependencies

```bash
npm install
```

### 2. Run the Python Backend Service

In a terminal, run:

```bash
python login_service.py
```

The service will start at `http://localhost:8000` and provide the `/login` endpoint.

**Credentials for testing:**
- Username: `user1`
- Password: `Password123`

### 3. Run the Angular Development Server

In another terminal, run:

```bash
npm start
```

This will start the Angular dev server at `http://localhost:4200`.

## Features

- **Reactive UI**: Uses Angular's template binding for real-time form updates
- **HTTP Client**: Communicates with the Python backend via `HttpClient`
- **Error Handling**: Graceful error handling with user-friendly messages
- **Responsive Design**: Same styling as the original HTML version
- **Loading States**: Visual feedback when credentials are being validated
- **Type Safety**: Full TypeScript support for better code quality

## Architecture

### Components
- **LoginComponent**: Main login form component with form handling and validation display

### Services
- **AuthService**: Handles HTTP communication with the Python backend

### Communication Flow
1. User enters credentials in the Angular login form
2. LoginComponent sends POST request via AuthService to `http://localhost:8000/login`
3. Python backend validates credentials against stored values
4. Backend responds with success/error status
5. Component displays appropriate message to user

## Development

### Build for Production

```bash
npm run build
```

This generates an optimized production build in the `dist/` directory.

### Running Tests

```bash
npm run test
```

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Notes

- The Python service is configured to accept CORS requests from the Angular frontend
- The application uses standalone Angular components (Angular 14+)
- The service validates credentials: use `user1` and `Password123` for successful login
