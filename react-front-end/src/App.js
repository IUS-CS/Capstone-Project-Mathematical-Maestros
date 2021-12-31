import Navbar from "./components/Navbar/Navbar"
import Home from "./pages/home";
import About from "./pages/about"
import SignUp from "./pages/signUp"
import SignIn from "./pages/signIn"

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {

  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/about' element={<About/>} />
        <Route path='/signUp' element={<SignUp/>} />
        <Route path='/signIn' element={<SignIn/>} />
      </Routes>
    </Router>
  );
}
export default App;