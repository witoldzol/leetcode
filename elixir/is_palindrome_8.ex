defmodule Solution do
  @spec is_palindrome(x :: integer) :: boolean
  def is_palindrome(x) do
    IO.puts("#{x} is #{Integer.to_charlist(x) |> Enum.reverse() == Integer.to_charlist(x)}")
  end
end

Solution.is_palindrome(5553)
Solution.is_palindrome(3553)
