function check_form() {
  var username = document.getElementById("name").value;
  var phone = document.getElementById("phone").value;

  var reg = /^\d{3}-\d{3,4}-\d{4}$/

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

  var elem = document.getElementById('form1');
  elem.submit();
};