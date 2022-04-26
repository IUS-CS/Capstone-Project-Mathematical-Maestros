import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar/Navbar"
import Home from "./pages/home";
import SignUp from "./pages/signUp"
import SignIn from "./pages/signIn"

const App = () => {

  return (
    <>
    <Router>
      <Navbar />
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/signUp' element={<SignUp/>} />
        <Route path='/signIn' element={<SignIn/>} />
      </Routes>
    </Router>
    </>
  );
}
export default App;