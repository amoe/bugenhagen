#! /usr/bin/perl
use strict;
use warnings;
use v5.20.2;
use Data::Dump qw/dump/;
use File::Slurper qw/read_text/;
use Getopt::Long;
use autodie qw(:all);
use Log::Any qw($log);
use Log::Dispatch;
use Log::Any::Adapter;


sub init_logging {
    # Send all logs to Log::Dispatch
    my $dispatch_logger = Log::Dispatch->new(
        outputs => [
            [ 'Screen', min_level => 'debug', newline => 1 ],
        ],
    );
    Log::Any::Adapter->set('Dispatch', dispatcher => $dispatch_logger);
}

init_logging();
$log->debugf("arguments are: %s", "foo");


my $data   = "file.dat";
my $length = 24;
my $verbose;

GetOptions ("length=i" => \$length,    # numeric
            "file=s"   => \$data,      # string
            "verbose"  => \$verbose)   # flag
    or die("Error in command line arguments\n");

sub main {
    say "Starting.";
    my $i = 1;
    for my $arg (@_) {
        say qq{<item id="c${i}"
href="$arg"
media-type="text/html"/>};
        $i++;
    }

    my $j = 1;
    for my $arg2 (@_) {
        say qq{<itemref idref="c${j}"/>};
        $j++;
    }

    say "End.";
}

main @ARGV;
