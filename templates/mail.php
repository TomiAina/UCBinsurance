<?php
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];
$from = 'From: Website';
$to = 'tomiomega50@yahoo.com';
$subject = 'Email Inquiry';

$body = "From: $name\n E-Mail: $email\n Message:\n $message";?>

<?php
if ($_POST['submit']) {
if (mail ($to, $subject, $body, $from)) {
echo '<p>Thank you for your message! </p>';
} else {
echo '<p>An error occurred. Try sending your message again.</p>'; }}?>

