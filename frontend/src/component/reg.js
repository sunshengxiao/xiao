import React from "react"
import {Link,Redirect} from "react-router-dom"
import '../css/login.css'
import axios from 'axios'
import store from 'store'
import userSer from "../../service/user"
import {message} from 'antd'
import 'antd/lib/message/style'
import {observer} from 'mobx-react'

store.addPlugin(require('store/plugins/expire'))

export default class Reg extends React.Component{      
    render(){ 
        return <_Reg service={userSer}/>
        }
    }
@observer
class _Reg extends React.Component{
    handleClick(event){
        event.preventDefault();
        let fm=event.target.form;
        this.props.service.reg(
            fm[0].value,fm[1].value,fm[2].value
        );
        }
    render(){
        if (this.props.service.loggedin){
            return <Redirect to = ""/>;//跳转
        }
        if (this.props.service.errorMsg){
            message.info(this.props.errorMsg,3,
                ()=>setTimeout(()=>this.props.service.errorMsg=''),1000)
        }
        return(<div><form className=" register- form">
    <input type= "text" placeholder="用户名"/>
    <input type= "text" placeholder="邮箱"/>
    <input type= "password" placeholder="密码"/>
    <button onClick={this.handleClick.bind(this)}> 注册</button>
    <p className="message">已注册? <Link to="./login">登录</Link></p>
    </form>
    </div>)
    }
};



