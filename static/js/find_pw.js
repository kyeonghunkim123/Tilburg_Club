function check_form2() {
  var ID = document.getElementById("ID").value;
  var phone = document.getElementById("phone").value;

  var reg = /^\d{3}-\d{3,4}-\d{4}$/;

  if (ID === "" && phone === "") {  // === 데이터 타입과 값이 모두 일치하는지 검사하는 비교 연산자 &&은 모두 참일때만 반환
    alert("아이디와 휴대전화번호를 입력해주세요.");
    return false;
  }

  if (ID === "") {
    alert("ID를 입력해주세요.");
    document.getElementById("ID").focus();
    return false;
  }

  if (phone === "" || !reg.test(phone))  {
    alert("휴대전화번호를 제대로 입력해주세요.");
    document.getElementById("phone").focus();
    return false;
  }

  if (ID === "" && phone === "") {
    alert("아이디와 휴대전화번호를 입력해주세요.");
    return false;
  }

  var elem=document.getElementById("form2").submit();
  elem.submit();
}