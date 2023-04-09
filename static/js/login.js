function check_form() {
 var form= document.forms['login-form'];
 if(form.ID.value =='gitcha2' && form.password.value=="1234")
 {
   window.open('main.html');
   return true;
 }
 else{
       alert("아이디랑 비밀번호를 확인해 주세요");
       return false;
 }
}
