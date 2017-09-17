// Strategy: lcm n ( lcm n-1 ( .. lcm 2 1)
open System

// greatest common divisor
let rec gcd a b =
    if b = 0 then
        abs a
    else
        gcd b (a % b)

// lowest common multiplier      
let lcm (a:int) (b:int) =
    abs a * b / gcd a b

// compose a list of functions fs into a single function
// lcm 4 ( lcm 3 ( lcm 2 ) )
let compose fs = List.reduce (>>) fs

[<EntryPoint>]
let main args =
    let n = Console.ReadLine() |> int
    for i in 1..n do
        let x = Console.ReadLine() |> int
        let fs = [for i in 2..x -> lcm i]
        if List.isEmpty fs then
            printfn "1"
        else
            let res = compose fs 1  
            printfn "%d" res
    0