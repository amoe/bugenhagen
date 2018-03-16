#! /usr/bin/perl
use strict;
use warnings;
use v5.20.2;
use Data::Dump qw/dump/;
use File::Slurper qw/read_text/;
use Getopt::Long;
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

my @inputs = (
    "content/salvage.zone/in-print/salvage-perspectives-3-or-whats-a-hell-for/index.html",
    "content/salvage.zone/in-print/neither-westminster-nor-brussels/index.html",
    "content/salvage.zone/in-print/technically-female-women-machines-and-hyperemployment/index.html",
    "content/salvage.zone/online-exclusive/the-realism-of-audacity-rethinking-revolutionary-strategy-today/index.html",
    "content/salvage.zone/in-print/corbyn-labour-and-the-present-crisis/index.html",
    "content/salvage.zone/in-print/the-political-is-political-in-conversation-with-yasmin-nair/index.html",
    "content/salvage.zone/in-print/white-overseers-of-the-world/index.html",
    "content/salvage.zone/in-print/year-v/index.html",
    "content/salvage.zone/in-print/from-choice-to-polarity-politics-of-in-and-and-art/index.html",
    "content/salvage.zone/articles/extract-from-blacklivesmatter-to-black-liberation/index.html",
    "content/salvage.zone/in-print/the-new-swedish-fascism-an-introduction/index.html",
    "content/salvage.zone/in-print/finance-economics-and-politics/index.html",
    "content/salvage.zone/in-print/the-abasement-of-trauma/index.html",
    "content/salvage.zone/in-print/benghazi/index.html"
);

sub main {
    say "Starting driver script.";
    for my $arg (@inputs) {
        say $arg;
        system("tidy -numeric -asxhtml -indent -modify -utf8 --add-xml-decl yes '$arg'");
        system("perl extract-article.perl '$arg' | sponge '$arg'");
        system("tidy -numeric -asxhtml -indent -modify -utf8 --add-xml-decl yes '$arg'");
    }
    say "Driver script finished.";
}

main @ARGV;
