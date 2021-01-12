# Brainfuck Interpreter

A couple of interpreters I've written for the brainfuck language. 

The Go implementation is roughly 5 times faster than the Python implementation on Pypy3,
though they're written similarly.


### Building the Go Interpreter 

```
go build -o bf bf.go
```

### Usage (Go)

```
./bf file
```

### Usage (Python)

```
python3 bf.py 
```
(If pypy3 is not installed on the system)

```
./bf.py
```
(if pypy3 is installed on the system)