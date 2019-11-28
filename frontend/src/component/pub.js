import React from "react"
import {Link,Redirect} from "react-router-dom"
import postSer from "../../service/post"
import {message} from 'antd'
import {Form,Input,Button} from 'antd'
import FormItem from 'antd/lib/form/FormItem'
import 'antd/lib/form/style'
import 'antd/lib/input/style'
import 'antd/lib/button/style'
import 'antd/lib/message/style'
import {observer} from 'mobx-react'
const {TextArea} = Input;

@observer
class _Pub extends React.Component{
    handelSubmit(event){
        event.preventDefault();
        console.log(event.target.form);
        let fm=event.target;
        this.props.service.pub(
            fm[0].value,fm[1].value
        )
        }
        render(){
        // if (this.props.service.loggedin){
        //     return <Redirect to = "/"/>;//跳转
        // }
        if (this.props.service.errorMsg){
            message.success(this.props.service.errorMsg, 3,()=>setTimeout(()=>this.props.service.errorMsg=''),1000)
            };
        return (
        <Form layout='horizontal' onSubmit={this.handelSubmit.bind(this)}>
            <FormItem label='标题' labelCol={{span:4}} wrapperCol={{span:12}}>
        <Input placeholder="标题" />
    </FormItem>
    <FormItem label='内容' labelCol={{span:4}} wrapperCol={{span:12}}>
        <TextArea rows={10} placeholder='内容'/>
    </FormItem>
    <FormItem  wrapperCol={{span:12,offset:13}}>
        <Button type='primary' htmlType='submit'>提交</Button>
    </FormItem>
      </Form>)
}
}
export default class Pub extends React.Component{
    render(){
    return <_Pub service={postSer}/>;    
    }}