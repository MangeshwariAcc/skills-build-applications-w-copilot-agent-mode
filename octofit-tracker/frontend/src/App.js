


import './App.css';
import { NavLink, Routes, Route } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import logo from './octofitapp-small.png';


function App() {
  return (
    <div className="App d-flex" style={{minHeight: '100vh'}}>
      <nav className="sidebar d-flex flex-column align-items-center py-4">
        <NavLink className="navbar-brand d-flex align-items-center fw-bold mb-4" to="/">
          <img src={logo} alt="Octofit Logo" style={{height: '48px', marginRight: '10px', background: '#fff', borderRadius: '8px', padding: '2px 6px'}} />
          Octofit Tracker
        </NavLink>
        <ul className="nav flex-column w-100">
          <li className="nav-item w-100"><NavLink className="nav-link" to="/activities">Activities</NavLink></li>
          <li className="nav-item w-100"><NavLink className="nav-link" to="/leaderboard">Leaderboard</NavLink></li>
          <li className="nav-item w-100"><NavLink className="nav-link" to="/teams">Teams</NavLink></li>
          <li className="nav-item w-100"><NavLink className="nav-link" to="/users">Users</NavLink></li>
          <li className="nav-item w-100"><NavLink className="nav-link" to="/workouts">Workouts</NavLink></li>
        </ul>
      </nav>
      <main className="flex-grow-1 d-flex align-items-center justify-content-center">
        <div className="container py-4">
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/" element={<div className="text-center"><h1 className="display-4 mb-3">Welcome to Octofit Tracker!</h1><p className="lead">Track your fitness, join teams, and compete on the leaderboard.</p></div>} />
          </Routes>
        </div>
      </main>
    </div>
  );
}

export default App;
