function check_form() {
    var user_ID = document.getElementsByName("ID")[0].value;
    var user_password = document.getElementsByName("password")[0].value;
    var user_id = "{{request.session.user_id}}";
    if (user_id == null){
      alert("아이디가 틀렸습니다.");}
    else{console.log(user_ID);}
    }

아이디를 다르게 입력했을 때 에러 메시지가 출력되지 않는 이유는, 서버 측에서 해당 오류를 처리하는 로직이 구현되어 있지 않기 때문일 수 있습니다.

제가 작성한 코드에서는 response.ok가 false인 경우에 에러 메시지를 던지도록 구현했기 때문에, 이 경우에도 서버 측에서 에러 응답을 보내주어야 합니다.

서버 측 코드를 확인해보시고, 해당 오류를 처리하는 로직이 없다면 구현해주셔야 합니다.
