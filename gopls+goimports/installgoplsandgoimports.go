package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"os/user"
	"strings"
)

func main() {
	// Get host username
	user, err := user.Current()
	if err != nil {
		log.Println(err)
	}

	username := user.Username
	godir := fmt.Sprintf("/home/%s/go/bin", username)
	profile := fmt.Sprintf("/home/%s/.profile", username)

	// Check if dir exists
	if _, err := os.Stat(godir); os.IsNotExist(err) {
		// If dir doesn't exist, install gopls and goimports
		cmd := exec.Command("go", "get", "-v", "golang.org/x/tools/gopls")
		cmd2 := exec.Command("go", "get", "-v", "golang.org/x/tools/cmd/goimports")

		err := cmd.Run()
		if err != nil {
			log.Fatalln(err)
		}
		fmt.Println("installed gopls.")

		err = cmd2.Run()
		if err != nil {
			log.Fatalln(err)
		}
		fmt.Println("installed goimports.")

		// It would be assumed that /usr/local/bin/go is added (if you can run this file). Now ~/go/bin needs to be added to PATH.

		// https://stackoverflow.com/a/26153102
		c, err := ioutil.ReadFile(profile)
		if err != nil {
			log.Println(err)
		}
		lines := strings.Split(string(c), "\n")
		for linenum, content := range lines {
			if strings.Contains(content, "export PATH=") {
				lines[linenum] = content + ":" + godir
				break
			}
		}
		output := strings.Join(lines, "\n")
		err = ioutil.WriteFile(profile, []byte(output), 0644)
		if err != nil {
			log.Println(err)
		}
		fmt.Printf("added %s to PATH.\n", godir)

		_ = exec.Command("source", ".profile").Run()
	}
}
