import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import AddSongForm from '../components/AddSongForm/AddSongForm';
import Layout from './Layout';
import LandingPage from '../components/LandingPage/LandingPage';
import ProfilePage from '../components/ProfilePage/ProfilePage';
import AlbumPage from '../components/AlbumPage/AlbumPage'




export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <LandingPage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "songs/new",
        element: <AddSongForm />,
      },
      {
        path: "profile",
        element: <ProfilePage />,
      },
      {
        path: "albums/:albumId",
        element: <AlbumPage />,
      },
    ],
  },
]);
