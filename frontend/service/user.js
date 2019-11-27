import axios from "axios";
import store from "store"
import {observable} from 'mobx'
store.addPlugin(require('store/plugins/expire'));
class UserService{
    @observable loggedin=false;
    @observable errorMsg="";
    login (email,password){
        console.log(email,password);
        axios.post("/api/user/login/",{email:email,password:password})/*devserver 代理*/
        .then(response=>{
            console.log(response);
            console.log(response.data);
            console.log(response.status);
            store.set("token",response.data.token,(new Date().getTime()+(8*3600*1000)));
            this.loggedin=true
            console.log(response.statusText);
            console.log(Headers);
            console.log(response.config);
        }).catch(error=> {
            console.log(error,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            this.errorMsg="登录失败，请稍后重试"
        }
        )
    };
    reg(name,email,password){
        console.log(email,password);
        axios.post('api/user/reg/',{email:email,name:name,password:password}
        ).then(response=>{
            console.log(response.data);
            console.log(response.status);
            store.set("token",response.data.token,(new Date().getTime()+(8*3600*1000)));
            this.loggedin=true
        }).catch(error=> {
                console.log(error)
                this.errorMsg='注册失败 请稍后重试'}
        )
    }
}
const userSer=new UserService();
export default userSer;