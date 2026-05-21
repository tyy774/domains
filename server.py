<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Сервер OKAKMINE | Выбор оплаты</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="img/favicon.ico" type="image/x-icon">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<button type="button" onclick="cancelPayment()" class="btn-back">Отмена</button><div class="cen"><h2>Выберите способ оплаты</h2></div>

<div class="checkout-container">

    <!-- выбор способа -->
    <label class="black">Способ оплаты:</label>
    <select id="paymentMethod">
        <option value="qr">QR-код</option>
        <option value="phone">По номеру телефона</option>
    </select>

    <!-- QR -->
    <div id="qrBlock">
        <p class="black">Отсканируйте QR:</p>
        <img src="img/QR.jpg" style="width:250px;">
    </div>

    <!-- телефон -->
    <div id="phoneBlock" style="display:none;">
        <p class="black">Перевод по номеру:</p>
        <b class="black">+7 922 252 00-55</b>
    </div>

    <hr>

    <!-- форма -->
    <form id="manualForm" enctype="multipart/form-data">
        <input type="text" id="name" placeholder="Nickname(имя на сервере)" required><br><br>
        <input type="email" id="email" placeholder="Email" required><br><br>

        <input type="text" id="product" readonly><br><br>
        <input type="text" id="price" readonly><br><br>

        <label class="black">Загрузите чек:</label>
        <input type="file" id="receipt" accept="image/*" required class="black"><br><br>

        <button type="submit" class="product-card__button">
            Отправить чек
        </button>
    </form>

</div>

<script>
// переключение методов
document.getElementById("paymentMethod").addEventListener("change", function() {
    if (this.value === "qr") {
        document.getElementById("qrBlock").style.display = "block";
        document.getElementById("phoneBlock").style.display = "none";
    } else {
        document.getElementById("qrBlock").style.display = "none";
        document.getElementById("phoneBlock").style.display = "block";
    }
});

// подставляем товар
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("product").value =
        localStorage.getItem("checkoutProductName");

    document.getElementById("price").value =
        localStorage.getItem("checkoutProductPrice");
});

// отправка формы
document.getElementById("manualForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const fileInput = document.getElementById("receipt");

    if (!fileInput.files.length) {
        alert("Загрузи чек!");
        return;
    }

    const formData = new FormData();
    formData.append("name", document.getElementById("name").value);
    formData.append("email", document.getElementById("email").value);
    formData.append("product", document.getElementById("product").value);
    formData.append("price", document.getElementById("price").value);
    formData.append("receipt", fileInput.files[0]);

    const res = await fetch("save_order.php", {
        method: "POST",
        body: formData
    });

    window.location.href = "thank_you.html";
});
</script>
<script>
function cancelPayment() {
    // очищаем выбранный товар
    localStorage.removeItem("checkoutProductName");
    localStorage.removeItem("checkoutProductPrice");

    // возврат в магазин
    window.location.href = "/shop";
}
</script>
</body>
</html>