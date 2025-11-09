<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    // Check credentials
    if ($username === "admin" && $password === "admin@123") {
        // Send HTTP 200 OK
        http_response_code(200);
        echo "<h2 style='color:green; text-align:center;'>✅ Login Successful (200 OK)</h2>";
    } else {
        // Send HTTP 404 Not Found
        http_response_code(404);
        echo "<h2 style='color:red; text-align:center;'>❌ 404 Not Found - Invalid Credentials!</h2>";
    }
} else {
    // Method not allowed
    http_response_code(405);
    echo "<h2 style='color:orange; text-align:center;'>⚠️ Method Not Allowed</h2>";
}
?>

