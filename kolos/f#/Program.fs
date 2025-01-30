open System

let rec product multL =
    match multL with
    | [] -> 1.0
    | x :: xs -> x * product xs

[<EntryPoint>]
let main argv =
    printfn "daj cos do mnzoenia:"
    let inL = Console.ReadLine()
    match inL with
    | null -> printfn "musisz cos dac"; 0
    | _ ->
        try
            let num = inL.Split(' ') |> Array.map float |> List.ofArray
            let result = product num
            printfn "wynik %f" result
            0
        with
        | :? FormatException ->
            printfn "musza byc tylko liczby"
            0

