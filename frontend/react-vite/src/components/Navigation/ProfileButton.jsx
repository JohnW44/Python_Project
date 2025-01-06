import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FaUserCircle } from 'react-icons/fa';
import { thunkLogin, thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
// import { Navigate, NavLink } from "react-router-dom";
import "./ProfileButton.css";
import {useNavigate} from "react-router-dom"

function ProfileButton() {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((store) => store.session.user);
  const ulRef = useRef();
  const navigate = useNavigate()

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const logout = (e) => {
    e.preventDefault();
    dispatch(thunkLogout());
    closeMenu();
  };

  //demo is corrupted must signupo with new demo acc and set here
  const demoLogin = (e) => {
    e.preventDefault();
    dispatch(thunkLogin({email: "demo@aa.io", password: "password"}))
    // dispatch(thunkLogin({email: "dan@dan.com", password: "dan"}))
    closeMenu()
  }

  const goSettings =() => {
    navigate('/profile');
    closeMenu()
  }

  return (
    <>
      <button onClick={toggleMenu}>
        <FaUserCircle className="icon" />
      </button>
      {showMenu && (
        <ul className={"profile-dropdown"} ref={ulRef}>
          {user ? (
            <>
              <li>Hey {user.username}</li>
              <li>{user.email}</li>
              <li>
                <button onClick={goSettings}>Profile Page</button> {/* Changed NavLink to button */}
              </li>
              <li>
                <button onClick={logout}>Log Out</button>
              </li>
            </>
          ) : (
            <>
              <OpenModalMenuItem
                itemText="Log In"
                onItemClick={closeMenu}
                modalComponent={<LoginFormModal />}
              />
              <OpenModalMenuItem
                itemText="Sign Up"
                onItemClick={closeMenu}
                modalComponent={<SignupFormModal />}
              />
              <li>
                <button onClick={demoLogin}>Demo User</button>
              </li>
            </>
          )}
        </ul>
      )}
    </>
  );
}

export default ProfileButton;
