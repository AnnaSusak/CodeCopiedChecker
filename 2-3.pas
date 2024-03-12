
Const
  Rows = 5;
  Cols = 5;
  Rnd  = 10;




var i,j : integer;

    M : array [1..Rows] of array [1..Cols] of integer;
//======================================================    



begin
  
  For i := 1 to Rows do
    For j := 1 to Cols do
      M[i,j] := random(Rnd);
      
  Writeln('Не очень красивая матрица');
  
  Writeln(M);
  
  Writeln;
  
  For i := 1 to Rows do
    begin
      For j := 1 to Cols do
        begin

                   Write(M[i,j]:3);

        end;
      Writeln;
    end;  
  
            
  
end.


