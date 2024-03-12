
Const
  Rows = 5;
  Cols = 5;
  Rnd  = 10;




var i,j : integer;

    A : array [1..Rows] of array [1..Cols] of integer;
//======================================================    



begin
  
  For k := 1 to Rows do
    For l := 1 to Cols do
      M[i,j] := random(Rnd);
      
  Writeln('Не очень красивая матрица');
  
  Writeln(A);
  
  Writeln;
  
  For i := 1 to Rows do
    begin
      For j := 1 to Cols do
        begin

                   Write(A[i,j]:3);

        end;
      Writeln;
    end;  
  
            
  
end.


