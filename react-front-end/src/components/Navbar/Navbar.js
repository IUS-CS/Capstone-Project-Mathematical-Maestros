import React from 'react';
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
				Home
			</NavLink>
			<NavLink to='/about' activeStyle>
				About Us
			</NavLink>
			<NavLink to='/signUp' activeStyle>
				Sign Up
			</NavLink>
		</NavMenu>
		<NavBtn>
			<NavBtnLink to='/signin'>Sign In</NavBtnLink>
		</NavBtn>
	</Nav>
	</>
);
};

export default Navbar;
