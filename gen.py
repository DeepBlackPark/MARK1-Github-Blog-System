from sys import argv as a

def create(your_username):
  return {
    "index.html" : f"""<!DOCTYPE html>
<html>
  <head>
    <title> DEEP BLACK PARK </title>
  </head>
  <body>
    <h1> DEEP BLACK PARK </h1>
    <details>
      <summery> BLOG POST </summery>
      <div>
        <ol>
          <li> EMPTY </li>
        </ol>
      </div>
    </details>
    <details>
      <summery> BLOG WRITE </summery>
      <div>
        <li><a href = "https://{your_username}.github.io/ED170_R.html"> text file editor </a></li>
        <li><a href = "https://{your_username}.github.io/editor.html"> html input element </a></li>
      </div>
    </details>
    <details>
      <summery> etc files </summery>
      <div>
        <ol>
          <li> EMPTY </li>
        </ol>
      </div>
    </details>
  </body>
</html>""",
    "editor.html" : f"""<!DOCTYPE html>
<html>
  <head>
    <title> html input </title>
  </head>
  <body>
    <h1> TEXTAREA NOTEPAD </h1>
    <details>
      <summery> More </summery>
      <div>
        <a href = "https://{your_username}.github.io/"> back to the homepage </a>
      </div>
    </details>
    <textarea></textarea>
  </body>
</html>""",
    "ED170_R.html" : f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title> TEXT EDITOR </title>
    <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>  
    <style>
        .console-text {{
            color: green;
            font-family: 'Courier New', 'Lucida Console', monospace;
        }}
    </style>
  </head>
  <body>
    <py-script>
      input_text = Element("input_text")
      output_text = Element("output_text")
      your_usernames = "{your_username}"

      def form_filling(x):
        return f"https://{{your_usernames}}.github.io/ED170_R.html?v={{x}}"
      
      def function_add_text(*args):
        output_text.element.innerText = form_filling(input_text.value) 
    </py-script>    
    <main class = "container">
      <h1 class = ".console-text"> TEXT EDITOR </h1>
      <details class = ".console-text">
        <summery class = ".console-text"> More </summery>
        <div>
          <ol class = ".console-text">
            <li class = ".console-text">
              <a class = ".console-text" href = "https://{your_username}.github.io/"> back to the homepage </a>
            </li>
            <li class = ".console-text">
              <details class = ".console-text">
                <summery class = ".console-text"> using editor.html to edit text more comfortable way </summery>
                <div class = ".console-text">
                  <textarea class = ".console-text"></textarea>
                </div>
              </details>
            </li>
          </ol>
        </div>
      </details>
      <h3 id = "output_text"></h3>
      <div>
        <input id = "input_text" type="text" placeholder="input text">
        <button id = "add_text" pys-onClick ="function_add_text">Click</button>

        <script>
          const urlParams = new URLSearchParams(window.location.search);
          const initialValue = urlParams.get('v');
  
          if (initialValue) {{
              document.getElementById('input_text').value = initialValue;
          }}
        </script>
      </div> 
    </main>    
  </body>
</html>"""
  }

def gener(**json):
  for i, j in json.items():
    with open(i, 'w') as f: f.write(j)

init_site_FE = lambda x : gener(create(x))

def CLIGenCore(a):
  return a[1] if len(a) > 1 else input("you'r github username : ")

def CLI():
  init_site_FE(CLIGenCore(a))

main = CLI

if __name__ == "__main__": main()
