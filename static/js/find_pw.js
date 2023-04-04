function check_form2() {
  var username = document.getElementById("username").value; //메소드명
  var phone = document.getElementById("phone").value;

  var reg = /^\d{3}-\d{3,4}-\d{4}$/  //전화번호가 000-0000-0000

  if (username == "") {
    alert("이름을 입력해주세요.");
    username.focus();
    return false;
  };

  if (phone == "" || !reg.test(phone))  {
    alert("휴대전화번호를 제대로 입력해주세요.");
    username.focus();
    return false;
  };

  var elem = document.getElementById'form2');
  elem.submit();
};