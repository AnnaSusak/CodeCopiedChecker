
Const
  Rows = 10;
  Cols = 10;
  Rnd  = 5;

var i,j : integer;

    A : array [1..Rows] of array [1..Cols] of integer;
//======================================================    
begin
  
  For i := 1 to Rows do
    For j := 1 to Cols do
      M[i,j] := random(Rnd);
      
      
      
  Writeln('Не красивая матрица');    
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


