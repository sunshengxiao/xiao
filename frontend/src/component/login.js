import React from "react"
import {Link,Redirect} from "react-router-dom"
import '../css/login.css'
import userSer from '../../service/user'
import {observer} from 'mobx-react'
import {message,Notification} from 'antd'
import 'antd/lib/message/style'


@observer
class _Login extends React.Component{
    handleClick(event){
        event.preventDefault();
        let fm=event.target.form;
        this.props.service.login(
            fm[0].value,fm[1].value
        )
        }
    render(){
        if (this.props.service.loggedin){
            return <Redirect to = "/"/>;//跳转
        }
        if (this.props.service.errorMsg){
            Notification.open({
                message: 'Notification Title',
                description:
                  'This is the content of the notification. This is the content of the notification. This is the content of the notification.',
                onClick: () => {
                  console.log('Notification Clicked!');
                },
              });
            };
        return(
<div className="login-page">
<form className=" register- form">
<input type= "text" placeholder="邮箱"/>
<input type= "password" placeholder="密码"/>
<button onClick={this.handleClick.bind(this)}>登录</button>
<p className="message">未注册？<Link to ="/reg">注册</Link></p>
</form>
</div>)
}
}
export default class Login extends React.Component{
    render(){
    return <_Login service={userSer}/>;    
    }
}