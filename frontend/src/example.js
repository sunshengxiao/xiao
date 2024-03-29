import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Login from "./component/login"
import Reg from "./component/reg"

function Home() {
  return (
    <div>
      <h2>Home</h2>
    </div>
  );
}

function About() {
  return (
    <div>
      <h2>About</h2>
    </div>
  );
}
export default function BasicExample() {
    return (
      <Router>
        <div>
          <div>
            <li><Link to ="/">主页</Link></li>
            <li><Link to ="/login">登录</Link></li>
            <li><Link to ="/reg">注册</Link></li>
            <li><Link to ="/about">关于</Link></li>
          </div>
            <Route exact path="/" component={Home}/>
            <Route path="/about" component={About}/>
            <Route path="/login" component={Login}/>
            <Route path="/reg" component={Reg}/>
        </div>
      </Router>
    );
  }
