{ pkgs ? import <nixpkgs> { overlays = [ 
	
(self: super: {	
	python39Packages.opencv4 = super.python39Packages.opencv4.override {
		enableGtk2 = true;
		enableGStreamer = true;
		enableGtk3 = true;
	};
})
];

}}:

pkgs.mkShell {
	nativeBuildInputs = with pkgs; [
		python39
		python39Packages.opencv4
	];
	
	buildInputs = [
		
	];
	
	shellHook = ''
	'';
}

