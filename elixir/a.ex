case {1,2,3} do
  {4,5,6} -> "this wont match"
  {1,x,3} -> IO.puts(x)
  _ -> "this will match all"
end
