// 使い方：headタグ内に「<script src="~~~/js/ajax.js') }}"></script>」を記載

function send_to_python() {
    target = document.getElementById("js_output");
    target.innerHTML = "<br><h3>実行中〜少々お待ちください</h3>";

    $.ajax("/call_from_ajax", {
        type: "post",            // 連想配列をPOSTする
    }).done(function (received_data) {           // 戻ってきたのはJSON（文字列）
        var dict = JSON.parse(received_data);   // JSONを連想配列にする
        // 以下、Javascriptで料理する
        var answer = dict["answer"];
        $("#result").html(answer);              // html要素を書き換える
    }).fail(function () {
        console.log("失敗");
    });
};