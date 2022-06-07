package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {
    // colorReset := "\033[0m"

    // colorRed := "\033[31m"
    colorGreen := "\033[32m"
    // colorYellow := "\033[33m"
   //  colorBlue := "\033[34m"
    colorPurple := "\033[35m"
   // colorCyan := "\033[36m"
   // colorWhite := "\033[37m"


	url := "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history?referenceCurrencyUuid=yhjMzLPhuIDl&timePeriod=24h"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("X-RapidAPI-Host", "coinranking1.p.rapidapi.com")
	req.Header.Add("X-RapidAPI-Key", "18aaa5f225mshd2fd2c15294c380p1c254ajsn96439fe174f5")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(string(colorGreen),res)
	fmt.Println(string(colorPurple), string(body))

}
