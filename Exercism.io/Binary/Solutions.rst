Solutions
=========

Crystal
-------

.. code-block:: crystal

    module Binary
        extend self
      
        def to_decimal(binary : String) : Int
          raise Exception.new if binary.chars.any? { |e| !['0', '1'].includes?(e) }
          dec = 0
          binary.chars.reverse.each_with_index do |digit, index|
            dec += digit.to_i * (2 ** index) if digit == '1'
          end
          dec
        end
      end