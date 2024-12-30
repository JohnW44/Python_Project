import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import { useSelector } from "react-redux";
import "./Navigation.css";


function Navigation() {
  const sessionUser = useSelector(state => state.session.user);
  return (
    <ul>
      <li>
        <NavLink to="/">Home</NavLink>
      </li>
      {sessionUser && (
        <li>
          <NavLink to="/songs/new">Add Song</NavLink>
        </li>
      )}
      <li>
        <ProfileButton />
      </li>
    </ul>
  );
}


export default Navigation;
