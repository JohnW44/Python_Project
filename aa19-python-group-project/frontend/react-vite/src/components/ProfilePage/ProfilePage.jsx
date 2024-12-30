import { useEffect } from 'react'
import './ProfilePage.css'
import { thunkAuthenticate } from '../../redux/session';
import { useDispatch, useSelector} from 'react-redux';

function ProfilePage(){

const dispatch = useDispatch();
const user = useSelector(state => state.session.user)

useEffect(() => {
    dispatch(thunkAuthenticate())
}, [dispatch])



    return (
        <>
            <div className='profilebox'>
                <h1>Profile Page</h1>
                <div className='profileinfo'>
                    <img src={user.profile_image} className='profile-pic'/>
                    <div className='details'>
                        <p>Username: {user.username}</p>
                        <p>Email: {user.email}</p>
                        <p>First Name: {user.first_name}</p>
                        <p>Last Name: {user.last_name}</p>
                    </div>
                </div>
            </div>
        </>
    )
}


export default ProfilePage