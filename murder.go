package main

import (
	"fmt"
	"os"
	"os/exec"
	"sync"
	"time"
)

var mutex sync.Mutex

func writeAndSend(str string, num int) {
	fn := fmt.Sprintf("RJgo%d.c", num)
	str = fmt.Sprintf("#include<stdio.h>\nint main(){printf(\"%s\");}", str)
	mutex.Lock()
	fi, err := os.Create(fn)
	if err != nil {
		mutex.Unlock()
		fmt.Printf("err\n")
		return
	}
	fi.Write([]byte(str))
	fi.Close()
	mutex.Unlock()
	exec.Command("bash", "submit2.sh", fn).Start()
}

func liner(lines int, str string, num int) {
	for _, s := range []string{"yes", "no"} {
		for n := 1; n < 10000; n++ {
			if 0 < lines-1 {
				if str == "" {
					liner(lines-1, fmt.Sprintf("%s:%d\\n", s, n), num+n)
				} else {
					liner(lines-1, fmt.Sprintf("%s%s:%d\\n", str, s, n), num+n)
				}
			} else {
				if str == "" {
					go writeAndSend(fmt.Sprintf("%s:%d\\n", s, n), num+n)
				} else {
					go writeAndSend(fmt.Sprintf("%s%s:%d\\n", str, s, n), num+n)
				}
				time.Sleep(65 * time.Millisecond)
			}
		}
	}
}

func main() {
	lines := 200
	for i := 1; i < lines; i++ {
		liner(i, "", 0)
	}
}
