fn string_to_binary(input: &str) -> String {

    let mut binary_string: String = String::new();

    for c in input.chars() {
        let binary_repr = format!("{:08b}", c as u8);
        binary_string.push_str(&binary_repr);
        binary_string.push(' ');
    }

    binary_string.trim().to_string()

}

fn return_number() -> i32 {
    let number = 42;  // Replace with the desired number
    number
}
fn main() {
    let message: &str = "RedBlockBlue";
    let number = return_number();
    println!("Value in binary {}", string_to_binary(message));

    println!("Message is: {}, nubmer is {}", message, number);
}

