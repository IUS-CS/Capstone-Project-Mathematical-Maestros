import React from 'react';
import logo from './logo.png';

import {
Nav,
NavLink,
NavMenu,
NavBtn,
NavBtnLink,
} from './NavbarElements';

const Navbar = () => {
return (
	<>
	<Nav>
		<NavMenu>
			<NavLink to='/' activeStyle>
				<img src={logo} alt='logo' />
			</NavLink>
			<NavLink to='/about' activeStyle>
				About Us
			</NavLink>
			<NavLink to='/signUp' activeStyle>
				Sign Up
			</NavLink>
		</NavMenu>
		<NavBtn>
		  <NavBtnLink to='/signIn'>Sign In</NavBtnLink>
		</NavBtn>
	</Nav>
	</>
);
};

export default Navbar;
