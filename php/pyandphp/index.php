<?php
if (empty($_REQUEST['data'])) die;

$header = explode("\r\n", urldecode($_REQUEST['data']));

$agreement = explode(" ", $header[0]);
$method = $agreement[0];
if ($agreement[1][0] == 'h') {
    $url = $agreement[1];
} else {
    $url = explode(":", $header[1])[1] . $agreement[1];
}

$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_CONNECTTIMEOUT, 3);
curl_setopt($curl, CURLOPT_HEADER, TRUE);
curl_setopt($curl, CURLOPT_NOBODY, FALSE);
curl_setopt($curl, CURLOPT_HTTPHEADER, $header);
curl_setopt($curl, CURLOPT_HTTPHEADER, array("X-HTTP-Method-Override: " . $method));//设置HTTP头信息
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, FALSE);
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, FALSE);
curl_exec($curl);
curl_close($curl);
echo $url;