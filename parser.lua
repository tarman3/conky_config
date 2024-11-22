-- https://superuser.com/questions/178179/modify-conky-to-handle-variable-length-values
function conky_pad(number)
    data = conky_parse(number)
    output = string.format('%2i', data) -- add space to string with one symbol
    return output
end

function conky_nodecimal(number)
    -- number -> downspeedf - Download speed in KiB with one decimal
    data = conky_parse(number)
    round_data = math.floor(data+0.5)
    output = string.format('%1i', round_data)
    return output
end

function conky_divide(number)
    -- number -> divide 1000
    data = conky_parse(number)
    output = string.sub(data,1,2)
    -- output = number/1000
    return output
end

function conky_removeUnits(line)
    data = conky_parse(line)
    output = string.gsub(data,'GiB','')
    return output
end

function conky_battery(number)
    period = os.time() - conky_parse(number)
    return period
end

function conky_halfLine(data)
    s = conky_parse(data)
    output = string.sub(s,0,23)
    return output
end
