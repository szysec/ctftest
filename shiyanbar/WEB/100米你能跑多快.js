//100米你能跑多快？ 预备，跑！
//使用暴力猴插件或控制台
//题目链接，http://ctf5.shiyanbar.com/jia/
function getTextByName(name) {
	return document.getElementsByName(name)[0].innerText;
}
function fillTextByName(name, text) {
    var names = document.getElementsByName(name);
    names[0].value = text;
}
res = eval(getTextByName("my_expr").replace(/x/g,"*"));
fillTextByName("pass_key", res);
