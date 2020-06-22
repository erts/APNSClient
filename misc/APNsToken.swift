// 
// Created by Roman Tsymbaliuk.
// 
// Copyright 2020 Roman Tsymbaliuk. All rights reserved.
//

import Foundation

/// APNs token Data to String converter
struct APNsToken {
	
	let token: String
	
    /**
     Initializes a new APNsToken struct

     - Parameters:
        - data: Data recieved from APNs service

     - Returns: APNsToken with stored APNs device token
     */
	
	init(data: Data) {
		token = data.map{String(format: "%.2x", $0)}.joined()
		#if DEBUG
		print(String(format: "APNs device token: %@", token))
		#endif
	}
}