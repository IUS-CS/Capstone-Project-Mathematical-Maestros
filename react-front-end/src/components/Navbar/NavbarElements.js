import { NavLink as Link } from 'react-router-dom';
import styled from 'styled-components';

export const Nav = styled.nav`
background: #44BBA4; 
height: 85px;
display: flex;
justify-content: space-between;
padding: 0.2rem calc((100vw - 1000px) / 2);
z-index: 12;
`;

export const NavLink = styled(Link)`
color: #F6F7EB;
font-size: 1.5rem;
display: flex;
align-items: center;
text-decoration: none;
padding: 0 1rem;
height: 100%;
cursor: pointer;
&.active {
	color: #393E41;
}
`;

export const NavMenu = styled.div`
display: flex;
align-items: center;
margin-right: -24px;
`;

export const NavBtn = styled.nav`
display: flex;
align-items: center;
margin-right: 24px;
`;

export const NavBtnLink = styled(Link)`
border-radius: 4px;
background: #3F88C5;
padding: 10px 22px;
color: #F6F7EB;
outline: none;
border: none;
cursor: pointer;
transition: all 0.2s ease-in-out;
text-decoration: none;
margin-left: 24px;
&:hover {
	transition: all 0.2s ease-in-out;
	background: #fff;
	color: #393E41;
}
`;
